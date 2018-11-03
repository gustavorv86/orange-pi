#include <stdlib.h>
#include <stdio.h>

#include "gpio_lib.h"

int main()
{
    if(SETUP_OK!=sunxi_gpio_init()){
        printf("Failed to initialize GPIO\n");
        return -1;
    }

    if(SETUP_OK!=sunxi_gpio_set_cfgpin(SUNXI_GPA(1),OUTPUT)){
        printf("Failed to config GPIO pin\n");
        return -1;
    }

    int i,j;
    while(1) {
        sunxi_gpio_output(SUNXI_GPA(15),HIGH);
        if(sunxi_gpio_output(PD1,HIGH)){
            printf("Failed to set GPIO pin value\n");
            return -1;
        }

        usleep(50000);
        if(sunxi_gpio_output(SUNXI_GPA(1),LOW)){
            printf("Failed to set GPIO pin value\n");
            return -1;
        }
        usleep(50000);
    
    }
    sunxi_gpio_cleanup();

    return 0;
    
}


