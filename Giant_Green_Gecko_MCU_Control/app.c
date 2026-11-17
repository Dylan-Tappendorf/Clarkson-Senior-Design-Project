#include "app.h"

extern volatile uint32_t system_time_ms;
static uint16_t current_msg_number = 0;

static void uart_write_bytes(const uint8_t *data, size_t len) {
    for (size_t i = 0; i < len; i++) {
        USART_Tx(USART4, data[i]);
    }
}

static void delay_ms(uint32_t ms) {
    uint32_t start = system_time_ms;
    while ((system_time_ms - start) < ms) {
        __NOP();
    }
}

void app_init(void) {
    GPIO_PinModeSet(gpioPortA, 12, gpioModeDisabled, 0);
    GPIO_PinModeSet(gpioPortA, 13, gpioModeDisabled, 0);
}

void app_process_action(void) {
    int16_t sample_buffer[NUM_SAMPLES];

    // Capture the start timestamp before the sampling block
    uint32_t start_time_ms = system_time_ms;

    // Configure single channel hardware for burst (Using VI as example)
    ADC_InitSingle_TypeDef singleInit = ADC_INITSINGLE_DEFAULT;
    singleInit.reference = adcRefVDD;
    singleInit.resolution = adcRes12Bit;
    singleInit.acqTime = adcAcqTime4;
    singleInit.posSel = ADC_PIN_VI;

    ADC_InitSingle(ADC0, &singleInit);
    ADC0->SINGLEFIFOCLEAR = ADC_SINGLEFIFOCLEAR_SINGLEFIFOCLEAR;

    // 1. High-speed sampling loop (~1 MHz)
    for (int i = 0; i < NUM_SAMPLES; i++) {
        ADC_Start(ADC0, adcStartSingle);
        while (!(ADC0->STATUS & ADC_STATUS_SINGLEDV));

        uint32_t raw_adc = ADC_DataSingleGet(ADC0);

        // Convert 12-bit unsigned (0-4095) to 16-bit signed by centering at 0
        sample_buffer[i] = (int16_t)((int32_t)raw_adc - 2048);
    }

    // 2. Construct 11-Byte Header
    // [0]    : 8-bit message type
    // [1:2]  : 16-bit message number (Little Endian)
    // [3:6]  : 32-bit number of samples (Little Endian)
    // [7:10] : 32-bit start time since startup (Little Endian)
    uint8_t header[11];
    uint32_t num_samples_u32 = (uint32_t)NUM_SAMPLES;

    header[0] = MSG_TYPE_ADC_BURST;

    header[1] = (uint8_t)(current_msg_number & 0xFF);
    header[2] = (uint8_t)((current_msg_number >> 8) & 0xFF);

    header[3] = (uint8_t)(num_samples_u32 & 0xFF);
    header[4] = (uint8_t)((num_samples_u32 >> 8) & 0xFF);
    header[5] = (uint8_t)((num_samples_u32 >> 16) & 0xFF);
    header[6] = (uint8_t)((num_samples_u32 >> 24) & 0xFF);

    header[7] = (uint8_t)(start_time_ms & 0xFF);
    header[8] = (uint8_t)((start_time_ms >> 8) & 0xFF);
    header[9] = (uint8_t)((start_time_ms >> 16) & 0xFF);
    header[10] = (uint8_t)((start_time_ms >> 24) & 0xFF);

    // 3. Transmit header then binary payload
    uart_write_bytes(header, sizeof(header));
    uart_write_bytes((const uint8_t*)sample_buffer, sizeof(sample_buffer));

    current_msg_number++;

    // Brief delay to prevent swamping UART (adjust based on application needs)
    delay_ms(100);
}
