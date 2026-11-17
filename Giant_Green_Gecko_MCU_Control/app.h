#ifndef APP_H
#define APP_H

#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>

#include "em_device.h"
#include "em_chip.h"
#include "em_cmu.h"
#include "em_gpio.h"
#include "em_usart.h"
#include "em_adc.h"

// ADC Pin Assignments
#define ADC_PIN_VI  adcPosSelAPORT1XCH12  // EXP Header Pin 3
#define ADC_PIN_VQ  adcPosSelAPORT1YCH13  // EXP Header Pin 5

// Message configuration
#define NUM_SAMPLES 512
#define MSG_TYPE_ADC_BURST 0x01

void app_init(void);
void app_process_action(void);

#endif
