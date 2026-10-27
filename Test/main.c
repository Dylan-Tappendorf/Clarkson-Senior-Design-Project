#include "app.h"

#define ADC_CLOCK_HZ 16000000

static void init_clocks(void) {
    CMU_ClockEnable(cmuClock_HFPER, true);
    CMU_ClockEnable(cmuClock_GPIO, true);
    CMU_ClockEnable(cmuClock_USART4, true);
    CMU_ClockEnable(cmuClock_ADC0, true); //ADC0 Clock
}

//ADC0 Configuration
static void init_adc0(void) {
    ADC_Init_TypeDef adcInit = ADC_INIT_DEFAULT;

    adcInit.prescale = ADC_PrescaleCalc(ADC_CLOCK_HZ, 0);
    adcInit.timebase = ADC_TimebaseCalc(0);
    adcInit.warmUpMode = adcWarmupNormal;

    ADC_Init(ADC0, &adcInit);

    // Default configuration for single-ended conversions
    ADC_InitSingle_TypeDef adcInitSingle = ADC_INITSINGLE_DEFAULT;
    adcInitSingle.reference = adcRefVDD;    //3.3V VDD Reference
    adcInitSingle.resolution = adcRes12Bit; //12-bit resolution
    adcInitSingle.acqTime = adcAcqTime8;    //8 ADC clock cycles acquisition time

    ADC_InitSingle(ADC0, &adcInitSingle);
}

//UART Config
static void init_usart4(void) {
    USART_InitAsync_TypeDef usart_init = USART_INITASYNC_DEFAULT;
    usart_init.baudrate = 115200;
    usart_init.enable = usartEnable;

    USART_InitAsync(USART4, &usart_init);

    //UART Board Configs:
    //EFM32GG11 (BRD2204C) VCOM Pin Configuration: PH4 (TX), PH5 (RX), PE1 (VCOM Enable)
    GPIO_PinModeSet(gpioPortH, 4, gpioModePushPull, 1);
    GPIO_PinModeSet(gpioPortH, 5, gpioModeInput, 0);
    GPIO_PinModeSet(gpioPortE, 1, gpioModePushPull, 1);

    USART4->ROUTEPEN = USART_ROUTEPEN_RXPEN | USART_ROUTEPEN_TXPEN;
    USART4->ROUTELOC0 = (USART_ROUTELOC0_RXLOC_LOC4) | (USART_ROUTELOC0_TXLOC_LOC4);
}

//Main Process
int main(void) {
    CHIP_Init();

    init_clocks();
    init_usart4();
    init_adc0();

    app_init();

    while (1) {
        app_process_action();
    }
}
