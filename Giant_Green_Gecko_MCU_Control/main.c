#include "app.h"

#define ADC_CLOCK_HZ 16000000

// Global millisecond timestamp updated by SysTick
volatile uint32_t system_time_ms = 0;

void SysTick_Handler(void) {
    system_time_ms++;
}

static void init_clocks(void) {
    CMU_ClockEnable(cmuClock_HFPER, true);
    CMU_ClockEnable(cmuClock_GPIO, true);
    CMU_ClockEnable(cmuClock_USART4, true);
    CMU_ClockEnable(cmuClock_ADC0, true);
}

// ADC0 Configuration
static void init_adc0(void) {
    ADC_Init_TypeDef adcInit = ADC_INIT_DEFAULT;

    adcInit.prescale = ADC_PrescaleCalc(ADC_CLOCK_HZ, 0);
    adcInit.timebase = ADC_TimebaseCalc(0);
    adcInit.warmUpMode = adcWarmupNormal;

    ADC_Init(ADC0, &adcInit);

    // Single-ended conversions targeting ~1 MHz
    // 12-bit conversion takes 13 SAR clock cycles.
    // adcAcqTime4 (4 cycles) + 13 cycles = 17 cycles. 16MHz / 17 = ~941 kHz.
    // (Use adcAcqTime2 for ~1.06 MHz)
    ADC_InitSingle_TypeDef adcInitSingle = ADC_INITSINGLE_DEFAULT;
    adcInitSingle.reference = adcRefVDD;
    adcInitSingle.resolution = adcRes12Bit;
    adcInitSingle.acqTime = adcAcqTime4;

    ADC_InitSingle(ADC0, &adcInitSingle);
}

// UART Config
static void init_usart4(void) {
    USART_InitAsync_TypeDef usart_init = USART_INITASYNC_DEFAULT;
    usart_init.baudrate = 115200;
    usart_init.enable = usartEnable;

    USART_InitAsync(USART4, &usart_init);

    GPIO_PinModeSet(gpioPortH, 4, gpioModePushPull, 1);
    GPIO_PinModeSet(gpioPortH, 5, gpioModeInput, 0);
    GPIO_PinModeSet(gpioPortE, 1, gpioModePushPull, 1);

    USART4->ROUTEPEN = USART_ROUTEPEN_RXPEN | USART_ROUTEPEN_TXPEN;
    USART4->ROUTELOC0 = (USART_ROUTELOC0_RXLOC_LOC4) | (USART_ROUTELOC0_TXLOC_LOC4);
}

// Main Process
int main(void) {
    CHIP_Init();

    init_clocks();
    init_usart4();
    init_adc0();

    // Configure SysTick to trigger every 1ms for the timestamp
    SysTick_Config(CMU_ClockFreqGet(cmuClock_CORE) / 1000);

    app_init();

    while (1) {
        app_process_action();
    }
}
