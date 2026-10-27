################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../app.c \
../main.c 

OBJS += \
./app.o \
./main.o 

C_DEPS += \
./app.d \
./main.d 


# Each subdirectory must supply rules for building sources it contributes
app.o: ../app.c subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: GNU ARM C Compiler'
	arm-none-eabi-gcc -g -gdwarf-2 -mcpu=cortex-m4 -mthumb -std=c99 '-DDEBUG=1' '-DDEBUG_EFM=1' '-DEFM32GG11B820F2048GL192=1' '-DHFXO_FREQ=50000000' '-DSL_BOARD_NAME="BRD2204C"' '-DSL_BOARD_REV="A02"' '-DSL_COMPONENT_CATALOG_PRESENT=1' -I"C:\Users\alexa\SimplicityStudio\v5_workspace\Test\config" -I"C:\Users\alexa\SimplicityStudio\v5_workspace\Test\autogen" -I"C:\Users\alexa\SimplicityStudio\v5_workspace\Test" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/Device/SiliconLabs/EFM32GG11B/Include" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/common/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//hardware/board/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/CMSIS/Core/Include" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/service/device_init/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/middleware/glib/dmd" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/middleware/glib" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/emlib/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/middleware/glib/glib" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//hardware/driver/memlcd/src/lpm013m126a" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//hardware/driver/memlcd/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//hardware/driver/memlcd/inc/memlcd_usart" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/common/toolchain/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/service/system/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/service/sleeptimer/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/service/udelay/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//protocol/zigbee/stack/include" -Os -Wall -Wextra -mno-sched-prolog -fno-builtin -ffunction-sections -fdata-sections -imacrossl_gcc_preinclude.h -mfpu=fpv4-sp-d16 -mfloat-abi=softfp --specs=nano.specs -c -fmessage-length=0 -MMD -MP -MF"app.d" -MT"$@" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

main.o: ../main.c subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: GNU ARM C Compiler'
	arm-none-eabi-gcc -g -gdwarf-2 -mcpu=cortex-m4 -mthumb -std=c99 '-DDEBUG=1' '-DDEBUG_EFM=1' '-DEFM32GG11B820F2048GL192=1' '-DHFXO_FREQ=50000000' '-DSL_BOARD_NAME="BRD2204C"' '-DSL_BOARD_REV="A02"' '-DSL_COMPONENT_CATALOG_PRESENT=1' -I"C:\Users\alexa\SimplicityStudio\v5_workspace\Test\config" -I"C:\Users\alexa\SimplicityStudio\v5_workspace\Test\autogen" -I"C:\Users\alexa\SimplicityStudio\v5_workspace\Test" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/Device/SiliconLabs/EFM32GG11B/Include" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/common/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//hardware/board/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/CMSIS/Core/Include" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/service/device_init/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/middleware/glib/dmd" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/middleware/glib" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/emlib/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/middleware/glib/glib" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//hardware/driver/memlcd/src/lpm013m126a" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//hardware/driver/memlcd/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//hardware/driver/memlcd/inc/memlcd_usart" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/common/toolchain/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/service/system/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/service/sleeptimer/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/service/udelay/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//protocol/zigbee/stack/include" -Os -Wall -Wextra -mno-sched-prolog -fno-builtin -ffunction-sections -fdata-sections -imacrossl_gcc_preinclude.h -mfpu=fpv4-sp-d16 -mfloat-abi=softfp --specs=nano.specs -c -fmessage-length=0 -MMD -MP -MF"main.d" -MT"$@" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


