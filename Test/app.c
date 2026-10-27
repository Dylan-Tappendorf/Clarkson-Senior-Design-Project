#include "app.h"

static uint32_t sample_timestamp_ms = 0;

static void uart_putchar(char c) {
    USART_Tx(USART4, (uint8_t)c);
}

static void uart_puts(const char *str) {
    while (*str) {
        uart_putchar(*str++);
    }
}

static void delay_ms(uint32_t ms) {
    for (volatile uint32_t i = 0; i < ms * 2000; i++) {
        __NOP();
    }
}

static void format_voltage(char *buf, size_t size, float val) {
    char sign = (val < 0.0f) ? '-' : '+';
    float abs_val = fabsf(val);
    int int_part = (int)abs_val;
    int frac_part = (int)((abs_val - (float)int_part) * 100.0f + 0.5f);

    if (frac_part >= 100) {
        int_part += 1;
        frac_part = 0;
    }
    snprintf(buf, size, "%c%d.%02d", sign, int_part, frac_part);
}

//Vi and Vq sampling
void app_adc_read_pair(float *v_i_out, float *v_q_out) {
    ADC_InitSingle_TypeDef singleInit = ADC_INITSINGLE_DEFAULT;
    singleInit.reference = adcRefVDD;     //3.3V VDD Reference
    singleInit.resolution = adcRes12Bit;  //12-bit Resolution
    singleInit.acqTime = adcAcqTime8;     //8 ADC clock cycles acquisition time

    //Channel 1: Vi (PA12 / Pin 3)
    singleInit.posSel = ADC_PIN_VI;
    ADC_InitSingle(ADC0, &singleInit);
    ADC0->SINGLEFIFOCLEAR = ADC_SINGLEFIFOCLEAR_SINGLEFIFOCLEAR; //Clear FIFO
    ADC_Start(ADC0, adcStartSingle);
    while (!(ADC0->STATUS & ADC_STATUS_SINGLEDV));
    uint32_t raw_i = ADC_DataSingleGet(ADC0);

    //Channel 2: Vq (PA13 / Pin 5)
    singleInit.posSel = ADC_PIN_VQ;
    ADC_InitSingle(ADC0, &singleInit);
    ADC0->SINGLEFIFOCLEAR = ADC_SINGLEFIFOCLEAR_SINGLEFIFOCLEAR; //Clear FIFO
    ADC_Start(ADC0, adcStartSingle);
    while (!(ADC0->STATUS & ADC_STATUS_SINGLEDV));
    uint32_t raw_q = ADC_DataSingleGet(ADC0);

    *v_i_out = ((float)raw_i * 3.3f) / 4095.0f;
    *v_q_out = ((float)raw_q * 3.3f) / 4095.0f;
}

void app_init(void) {
    GPIO_PinModeSet(gpioPortA, 12, gpioModeDisabled, 0);
    GPIO_PinModeSet(gpioPortA, 13, gpioModeDisabled, 0);
    sample_timestamp_ms = 0;
}

void app_process_action(void) {
    char tx_buffer[160];
    char str_vi[16], str_vq[16], str_vctrl[16], str_phase[16];

    float v_i_raw = 0.0f;
    float v_q_raw = 0.0f;

    //Synchronous sample of both ADC channels
    app_adc_read_pair(&v_i_raw, &v_q_raw);

    //Centered AC voltages
    float v_i = v_i_raw - OFFSET_I;
    float v_q = v_q_raw - OFFSET_Q;

    //Vector Magnitude
    float v_ctrl = sqrtf((v_i * v_i) + (v_q * v_q));

    //Phase angle calculation
    float phase_rad = atan2f(v_q, v_i);
    float phase_deg = phase_rad * (180.0f / (float)M_PI);
    if (phase_deg < 0.0f) {
        phase_deg += 360.0f;
    }

    //Safe format
    format_voltage(str_vi, sizeof(str_vi), v_i);
    format_voltage(str_vq, sizeof(str_vq), v_q);
    format_voltage(str_vctrl, sizeof(str_vctrl), v_ctrl);

    int phase_int = (int)phase_deg;
    int phase_frac = (int)fabsf((phase_deg - (float)phase_int) * 100.0f + 0.5f);
    snprintf(str_phase, sizeof(str_phase), "%d.%02d", phase_int, phase_frac);

    int time_sec = sample_timestamp_ms / 1000;
    int time_ms = sample_timestamp_ms % 1000;

    snprintf(tx_buffer, sizeof(tx_buffer),
             "[%02d:%02d.%03d] Vi: %sV | Vq: %sV | Vctrl: %sV | Phase: %s deg\r\n",
             time_sec / 60, time_sec % 60, time_ms,
             str_vi, str_vq, str_vctrl, str_phase);

    uart_puts(tx_buffer);

}
