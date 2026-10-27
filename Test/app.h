#ifndef APP_H
#define APP_H

#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#define _USE_MATH_DEFINES
#include <math.h>

#ifndef M_PI
#define M_PI 3.14159265358979323846f
#endif

#include "em_device.h"
#include "em_chip.h"
#include "em_cmu.h"
#include "em_gpio.h"
#include "em_usart.h"
#include "em_adc.h"

//Midset DC Bias
#define OFFSET_I  1.65f
#define OFFSET_Q  1.65f

//ADC Pin Assignments
#define ADC_PIN_VI  adcPosSelAPORT1XCH12  //EXP Header Pin 3
#define ADC_PIN_VQ  adcPosSelAPORT1YCH13  //EXP Header Pin 5

void app_init(void);
void app_process_action(void);
float app_adc_read_voltage(ADC_PosSel_TypeDef input_pin);

#endif
