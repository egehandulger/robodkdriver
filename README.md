# RoboDK Robot Driver Boilerplate

## How to use?
1. Install library
    ```
    pip install robodkdriver
    
    ```

2. Create a python file in RoboDK driver directory

3. Import module
    ```
    from robodkdriver import RoboDK, RobotSerial
    
    ```

4. Extend `RobotSerial` class 
    ```
    class MyOneAxisRobot(RobotSerial):
        def run_command(self, cmd: str, args: tuple):
            RoboDK.update_status('working')
    
            if cmd == 'CONNECT':
                connected = self._connect(port=args[0], baud_rate=int(args[1]))
    
                if not connected:
                    return 'connection_problems'
    
                return 'ready'
    
            if cmd == 'DISCONNECT' or cmd == 'STOP':
                disconnected = self._disconnect()
    
                if disconnected:
                    return 'disconnected'
    
                return 'ready'
    
            if cmd == 'MOVJ':
                self._send_message('{cmd} {angle}'.format(cmd=cmd, angle=args[0]))
    
                if self._get_message('DONE'):
                    return 'ready'
    
                return 'error'
    
            if cmd == 'CJNT':
                self._send_message(cmd)
    
                joints = self._get_message()
                RoboDK.update_status(joints)
    
                return 'ready'
                
            ...
    
    ```
    
    You need to define how robot should act accordingly to each RoboDK command.
    You can return:
    - **ready**: when robot is ready for new command
    - **working**: when robot starts working
    - **waiting**: when robot is waiting
    - **disconnected**: when robot is disconnected
    - **not_connected**: when robot is not connected
    - **connection_problems**: when there are connection problems
    
5. Start driver
    ```
    if __name__ == '__main__':
        RoboDK(MyOneAxisRobot()).run_driver()
    
    ```

6. Change configuration on RoboDK robot connection

## TODO
1. RobotSocket Class
2. Better getting started
3. More info on how RoboDK driver communicates
