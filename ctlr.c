// Driver for parsing XBOX controller input. Xpad driver shold create device 
// at /dev/input/js0. There are two main types of input events button and
// analog. A button event is binary, it either is pressed or not and there are
// press and release events. Analog inputs have an associated analog value
// which denotes "how pressed" the analog stick. The triggers have a singlar
// value describing how pressed they are. The two joy sticks have analog values
// which can be used to determine the direction and how much the sticks are 
// moved in that direction.

#include <stdio.h>    // printf
#include <fcntl.h>    // open, O_RDONLY
#include <unistd.h>   // close, read

#define DEBUG 0
char* device_string = "/dev/input/js0";
int cmd_size = 0x8;

// CMD structure defines from XBOX ctlr
#define INPUT_TYPE_BYTE 6
#define BUTTON_ID_BYTE 7
#define INPUT_TYPE_BUTTON 1
#define BUTTON_EVENT_TYPE_BYTE 4
#define BUTTON_REL_ID 0
#define BUTTON_PRS_ID 1
#define A_BUTTON_ID 0
#define B_BUTTON_ID 1
#define X_BUTTON_ID 2
#define Y_BUTTON_ID 3
#define LB_BUTTON_ID 4
#define RB_BUTTON_ID 5
#define SEL_BUTTON_ID 6
#define STRT_BUTTON_ID 7
#define XBOX_BUTTON_ID 8
#define L3_BUTTON_ID 9
#define R3_BUTTON_ID 10
#define DL_BUTTON_ID 11
#define DR_BUTTON_ID 12
#define DU_BUTTON_ID 13
#define DD_BUTTON_ID 14

#define INPUT_TYPE_ANALOG 2
#define ANALOG_BYTE_1 4
#define ANALOG_BYTE_2 5
#define L_JOY_X 0 
#define L_JOY_Y 1
#define LT_ANALOG_ID 2
#define R_JOY_X 3        
#define R_JOY_Y 4
#define RT_ANALOG_ID 5

// Packet defintion for data sent to vehicle
#define 

int main()
{

    // Open device
    int ctlr_fd = open(device_string, O_RDONLY);
    if(ctlr_fd < 0)
    {
        printf("Failed to open XBOX device: %s\n", device_string);
        return 1;
    }

    // main loop
    int num_read = 0;
    char unsigned buff[cmd_size];
    while(1)
    {   
        //*********************************************************************
        // Read input command and check for errors
        //*********************************************************************
        num_read = read(ctlr_fd, buff, cmd_size);
        if(num_read < 0)
        {
            printf("Lost Connection to device\n");
            return 1;
        }
        if(num_read != cmd_size)
        {
            printf("Warning cmd buffer not filled, %d\n", num_read);
        }

        //*********************************************************************
        // Parse input into classes, analog and button
        //*********************************************************************
        #if !DEBUG
        if(buff[INPUT_TYPE_BYTE] == INPUT_TYPE_BUTTON)
        {
            unsigned char pressed = buff[BUTTON_EVENT_TYPE_BYTE];
            switch(buff[BUTTON_ID_BYTE])
            {
                case A_BUTTON_ID:
                    printf("A button event, pressed? %d \n", pressed);
                    break;
                case B_BUTTON_ID:
                    printf("B button event, pressed? %d \n", pressed);
                    break;
                case X_BUTTON_ID:
                    printf("X button event, pressed? %d \n", pressed);
                    break;
                case Y_BUTTON_ID:
                    printf("Y button event, pressed? %d \n", pressed);
                    break;
                case LB_BUTTON_ID:
                    printf("LB button event, pressed? %d \n", pressed);
                    break;
                case RB_BUTTON_ID:
                    printf("RB button event, pressed? %d \n", pressed);
                    break;
                case SEL_BUTTON_ID:
                    printf("SEL button event, pressed? %d \n", pressed);
                    break;
                case STRT_BUTTON_ID:
                    printf("STRT button event, pressed? %d \n", pressed);
                    break;
                case XBOX_BUTTON_ID:
                    printf("XBOX button event, pressed? %d \n", pressed);
                    break;
                case L3_BUTTON_ID:
                    printf("L3 button event, pressed? %d \n", pressed);
                    break;
                case R3_BUTTON_ID:
                    printf("R3 button event, pressed? %d \n", pressed);
                    break;
                case DL_BUTTON_ID:
                    printf("DL button event, pressed? %d \n", pressed);
                    break;
                case DR_BUTTON_ID:
                    printf("DR button event, pressed? %d \n", pressed);
                    break;
                case DU_BUTTON_ID:
                    printf("DU button event, pressed? %d \n", pressed);
                    break;
                case DD_BUTTON_ID:
                    printf("DD button event, pressed? %d \n", pressed);
                    break;
                default:
                    printf("WARNING unidentified button event\n");
            }
        }
        else if(buff[INPUT_TYPE_BYTE] == INPUT_TYPE_ANALOG)
        {
            unsigned char xval_1 = buff[ANALOG_BYTE_1];
            unsigned char xval_2 = buff[ANALOG_BYTE_2];
            short xval = (((short)xval_2) << 8) + ((short) xval_1);
            switch(buff[BUTTON_ID_BYTE])
            {
                case LT_ANALOG_ID:
                    printf("LT event, x = %d\n", xval);
                    break;
                case RT_ANALOG_ID:
                    printf("RT event, x = %d\n", xval);
                    break;
                case R_JOY_X:
                    printf("R joy X event, x = %d\n", xval);
                    break;
                case R_JOY_Y:
                    printf("R joy Y event, x = %d\n", xval);
                    break;
                case L_JOY_X:
                    printf("L joy X event, x = %d\n", xval);
                    break;
                case L_JOY_Y:
                    printf("L joy Y event, x = %d\n", xval);
                    break;

            }
        }
        else
        {
            printf("WARNING unkown input type parsed! code = %d\n", buff[INPUT_TYPE_BYTE]);
        }
        #endif
        //*********************************************************************
        // Debug output
        //*********************************************************************
        #if DEBUG
        int i;
        for(i = 0; i < cmd_size; ++i)
        {
            printf("%u ", buff[i]);
        }
        printf("\n");
        #endif
    }

    // Close device
    if(close(ctlr_fd))
    {
        printf("Failed to close XBOX device: %s\n", device_string);
        return 1;
    }

}