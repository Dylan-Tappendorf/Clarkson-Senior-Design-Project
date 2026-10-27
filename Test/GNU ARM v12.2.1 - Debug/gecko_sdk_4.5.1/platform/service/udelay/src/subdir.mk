################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk/platform/service/udelay/src/sl_udelay.c 

S_UPPER_SRCS += \
C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk/platform/service/udelay/src/sl_udelay_armv6m_gcc.S 

OBJS += \
./gecko_sdk_4.5.1/platform/service/udelay/src/sl_udelay.o \
./gecko_sdk_4.5.1/platform/service/udelay/src/sl_udelay_armv6m_gcc.o 

C_DEPS += \
./gecko_sdk_4.5.1/platform/service/udelay/src/sl_udelay.d 


# Each subdirectory must supply rules for building sources it contributes
gecko_sdk_4.5.1/platform/service/udelay/src/sl_udelay.o: C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk/platform/service/udelay/src/sl_udelay.c gecko_sdk_4.5.1/platform/service/udelay/src/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: GNU ARM C Compiler'
	arm-none-eabi-gcc -g -gdwarf-2 -mcpu=cortex-m4 -mthumb -std=c99 '-DDEBUG=1' '-DDEBUG_EFM=1' '-DEFM32GG11B820F2048GL192=1' '-DHFXO_FREQ=50000000' '-DSL_BOARD_NAME="BRD2204C"' '-DSL_BOARD_REV="A02"' '-DSL_COMPONENT_CATALOG_PRESENT=1' -I"C:\Users\alexa\SimplicityStudio\v5_workspace\Test\config" -I"C:\Users\alexa\SimplicityStudio\v5_workspace\Test\autogen" -I"C:\Users\alexa\SimplicityStudio\v5_workspace\Test" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/Device/SiliconLabs/EFM32GG11B/Include" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/common/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//hardware/board/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/CMSIS/Core/Include" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/service/device_init/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/middleware/glib/dmd" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/middleware/glib" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/emlib/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/middleware/glib/glib" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//hardware/driver/memlcd/src/lpm013m126a" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//hardware/driver/memlcd/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//hardware/driver/memlcd/inc/memlcd_usart" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/common/toolchain/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/service/system/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/service/sleeptimer/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/service/udelay/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//protocol/zigbee/stack/include" -Os -Wall -Wextra -mno-sched-prolog -fno-builtin -ffunction-sections -fdata-sections -imacrossl_gcc_preinclude.h -mfpu=fpv4-sp-d16 -mfloat-abi=softfp --specs=nano.specs -c -fmessage-length=0 -MMD -MP -MF"gecko_sdk_4.5.1/platform/service/udelay/src/sl_udelay.d" -MT"$@" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

gecko_sdk_4.5.1/platform/service/udelay/src/sl_udelay_armv6m_gcc.o: C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk/platform/service/udelay/src/sl_udelay_armv6m_gcc.S gecko_sdk_4.5.1/platform/service/udelay/src/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: GNU ARM Assembler'
	arm-none-eabi-gcc -g -gdwarf-2 -mcpu=cortex-m4 -mthumb -I"C:\Users\alexa\SimplicityStudio\v5_workspace\Test\config" -I"C:\Users\alexa\SimplicityStudio\v5_workspace\Test\autogen" -I"C:\Users\alexa\SimplicityStudio\v5_workspace\Test" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/Device/SiliconLabs/EFM32GG11B/Include" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/common/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//hardware/board/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/CMSIS/Core/Include" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/service/device_init/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/middleware/glib/dmd" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/middleware/glib" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/emlib/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/middleware/glib/glib" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//hardware/driver/memlcd/src/lpm013m126a" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//hardware/driver/memlcd/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//hardware/driver/memlcd/inc/memlcd_usart" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/common/toolchain/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/service/system/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/service/sleeptimer/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//platform/service/udelay/inc" -I"C:/Users/alexa/SimplicityStudio/SDKs/gecko_sdk//protocol/zigbee/stack/include" '-DDEBUG_EFM=1' '-DEFM32GG11B820F2048GL192=1' '-DHFXO_FREQ=50000000' '-DSL_BOARD_NAME="BRD2204C"' '-DSL_BOARD_REV="A02"' '-DSL_COMPONENT_CATALOG_PRESENT=1' -mfpu=fpv4-sp-d16 -mfloat-abi=softfp -imacrossl_gcc_preinclude.h -c -x assembler-with-cpp -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


