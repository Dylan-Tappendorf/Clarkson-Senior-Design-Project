################################################################################
# Automatically-generated file. Do not edit!
################################################################################

-include ../makefile.init

RM := rm -rf

# All of the sources participating in the build are defined here
-include sources.mk
-include gecko_sdk_4.5.1/platform/service/udelay/src/subdir.mk
-include gecko_sdk_4.5.1/platform/service/system/src/subdir.mk
-include gecko_sdk_4.5.1/platform/service/sleeptimer/src/subdir.mk
-include gecko_sdk_4.5.1/platform/service/device_init/src/subdir.mk
-include gecko_sdk_4.5.1/platform/middleware/glib/glib/subdir.mk
-include gecko_sdk_4.5.1/platform/middleware/glib/fonts/subdir.mk
-include gecko_sdk_4.5.1/platform/middleware/glib/dmd/display/subdir.mk
-include gecko_sdk_4.5.1/platform/emlib/src/subdir.mk
-include gecko_sdk_4.5.1/platform/common/toolchain/src/subdir.mk
-include gecko_sdk_4.5.1/platform/common/src/subdir.mk
-include gecko_sdk_4.5.1/platform/Device/SiliconLabs/EFM32GG11B/Source/subdir.mk
-include gecko_sdk_4.5.1/hardware/driver/memlcd/src/memlcd_usart/subdir.mk
-include gecko_sdk_4.5.1/hardware/driver/memlcd/src/subdir.mk
-include gecko_sdk_4.5.1/hardware/board/src/subdir.mk
-include autogen/subdir.mk
-include subdir.mk
-include objects.mk

ifneq ($(MAKECMDGOALS),clean)
ifneq ($(strip $(C_DEPS)),)
-include $(C_DEPS)
endif
endif

-include ../makefile.defs

OPTIONAL_TOOL_DEPS := \
$(wildcard ../makefile.defs) \
$(wildcard ../makefile.init) \
$(wildcard ../makefile.targets) \


BUILD_ARTIFACT_NAME := Test
BUILD_ARTIFACT_EXTENSION := axf
BUILD_ARTIFACT_PREFIX :=
BUILD_ARTIFACT := $(BUILD_ARTIFACT_PREFIX)$(BUILD_ARTIFACT_NAME)$(if $(BUILD_ARTIFACT_EXTENSION),.$(BUILD_ARTIFACT_EXTENSION),)

# Add inputs and outputs from these tool invocations to the build variables 

# All Target
all: main-build

# Main-build Target
main-build: Test.axf

# Tool invocations
Test.axf: $(OBJS) $(USER_OBJS) makefile objects.mk $(OPTIONAL_TOOL_DEPS)
	@echo 'Building target: $@'
	@echo 'Invoking: GNU ARM C Linker'
	arm-none-eabi-gcc -g -gdwarf-2 -mcpu=cortex-m4 -mthumb -T "C:\Users\alexa\SimplicityStudio\v5_workspace\Test\autogen\linkerfile.ld" -Wl,--no-warn-rwx-segments -Xlinker --gc-sections -Xlinker -Map="Test.map" -mfpu=fpv4-sp-d16 -mfloat-abi=softfp --specs=nano.specs -o Test.axf -Wl,--start-group "./app.o" "./main.o" "./autogen/sl_board_default_init.o" "./autogen/sl_device_init_clocks.o" "./autogen/sl_event_handler.o" "./gecko_sdk_4.5.1/hardware/board/src/sl_board_control_gpio.o" "./gecko_sdk_4.5.1/hardware/board/src/sl_board_init.o" "./gecko_sdk_4.5.1/hardware/driver/memlcd/src/memlcd_usart/sl_memlcd_spi.o" "./gecko_sdk_4.5.1/hardware/driver/memlcd/src/sl_memlcd.o" "./gecko_sdk_4.5.1/hardware/driver/memlcd/src/sl_memlcd_display.o" "./gecko_sdk_4.5.1/platform/Device/SiliconLabs/EFM32GG11B/Source/startup_efm32gg11b.o" "./gecko_sdk_4.5.1/platform/Device/SiliconLabs/EFM32GG11B/Source/system_efm32gg11b.o" "./gecko_sdk_4.5.1/platform/common/src/sl_assert.o" "./gecko_sdk_4.5.1/platform/common/src/sl_syscalls.o" "./gecko_sdk_4.5.1/platform/common/toolchain/src/sl_memory.o" "./gecko_sdk_4.5.1/platform/emlib/src/em_adc.o" "./gecko_sdk_4.5.1/platform/emlib/src/em_cmu.o" "./gecko_sdk_4.5.1/platform/emlib/src/em_core.o" "./gecko_sdk_4.5.1/platform/emlib/src/em_emu.o" "./gecko_sdk_4.5.1/platform/emlib/src/em_gpio.o" "./gecko_sdk_4.5.1/platform/emlib/src/em_msc.o" "./gecko_sdk_4.5.1/platform/emlib/src/em_rtc.o" "./gecko_sdk_4.5.1/platform/emlib/src/em_rtcc.o" "./gecko_sdk_4.5.1/platform/emlib/src/em_system.o" "./gecko_sdk_4.5.1/platform/emlib/src/em_timer.o" "./gecko_sdk_4.5.1/platform/emlib/src/em_usart.o" "./gecko_sdk_4.5.1/platform/middleware/glib/dmd/display/dmd_memlcd.o" "./gecko_sdk_4.5.1/platform/middleware/glib/fonts/glib_font_narrow_6x8.o" "./gecko_sdk_4.5.1/platform/middleware/glib/fonts/glib_font_normal_8x8.o" "./gecko_sdk_4.5.1/platform/middleware/glib/fonts/glib_font_number_16x20.o" "./gecko_sdk_4.5.1/platform/middleware/glib/glib/bmp.o" "./gecko_sdk_4.5.1/platform/middleware/glib/glib/glib.o" "./gecko_sdk_4.5.1/platform/middleware/glib/glib/glib_bitmap.o" "./gecko_sdk_4.5.1/platform/middleware/glib/glib/glib_circle.o" "./gecko_sdk_4.5.1/platform/middleware/glib/glib/glib_line.o" "./gecko_sdk_4.5.1/platform/middleware/glib/glib/glib_polygon.o" "./gecko_sdk_4.5.1/platform/middleware/glib/glib/glib_rectangle.o" "./gecko_sdk_4.5.1/platform/middleware/glib/glib/glib_string.o" "./gecko_sdk_4.5.1/platform/service/device_init/src/sl_device_init_dcdc_s1.o" "./gecko_sdk_4.5.1/platform/service/device_init/src/sl_device_init_emu_s1.o" "./gecko_sdk_4.5.1/platform/service/device_init/src/sl_device_init_hfxo_s1.o" "./gecko_sdk_4.5.1/platform/service/device_init/src/sl_device_init_lfxo_s1.o" "./gecko_sdk_4.5.1/platform/service/device_init/src/sl_device_init_nvic.o" "./gecko_sdk_4.5.1/platform/service/sleeptimer/src/sl_sleeptimer.o" "./gecko_sdk_4.5.1/platform/service/sleeptimer/src/sl_sleeptimer_hal_rtc.o" "./gecko_sdk_4.5.1/platform/service/sleeptimer/src/sl_sleeptimer_hal_rtcc.o" "./gecko_sdk_4.5.1/platform/service/sleeptimer/src/sl_sleeptimer_hal_timer.o" "./gecko_sdk_4.5.1/platform/service/system/src/sl_system_init.o" "./gecko_sdk_4.5.1/platform/service/system/src/sl_system_process_action.o" "./gecko_sdk_4.5.1/platform/service/udelay/src/sl_udelay.o" "./gecko_sdk_4.5.1/platform/service/udelay/src/sl_udelay_armv6m_gcc.o" -lgcc -lc -lm -lnosys -Wl,--end-group -Wl,--start-group -lgcc -lc -lnosys -Wl,--end-group
	@echo 'Finished building target: $@'
	@echo ' '

	@echo 'Building out file: Test.out'
	arm-none-eabi-objcopy "Test.axf" "Test.out"
	@echo ' '

	@echo 'Building hex file: Test.hex'
	arm-none-eabi-objcopy -O ihex "Test.axf" "Test.hex"
	@echo ' '

	@echo 'Building bin file: Test.bin'
	arm-none-eabi-objcopy -O binary "Test.axf" "Test.bin"
	@echo ' '

	@echo 'Building s37 file: Test.s37'
	arm-none-eabi-objcopy -O srec "Test.axf" "Test.s37"
	@echo ' '

	@echo 'Running size tool'
	arm-none-eabi-size "Test.axf" -A
	@echo ' '

# Other Targets
clean:
	-@$(foreach FILE, $(EXECUTABLES), $(shell $(RM) $(FILE)) )
	-@$(foreach FILE, $(OBJS), $(shell $(RM) $(FILE)) )
	-@$(foreach FILE, $(C_DEPS), $(shell $(RM) $(FILE)) )
	-$(RM) Test.axf
	-@echo ' '

.PHONY: all clean dependents main-build

-include ../makefile.targets
