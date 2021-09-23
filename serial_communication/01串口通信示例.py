"""
Methods of Serial instances:
    open()    # open port
    close()    # close port immediately
    setBaudrate(baudrate)    # change baud rate on an open port
    inWaiting()    # return the number of chars in the receive buffer
    read(size=1)    # read "size" characters
    write(s)    # write the string s to the port
    flushInput()    # flush input buffer, discarding all it's contents
    flushOutput()    # flush output buffer, abort output
    sendBreak()    # send break condition
    setRTS(level=1)    # set RTS line to specified logic level
    setDTR(level=1)    # set DTR line to specified logic level
    getCTS()    # return the state of the CTS line
    getDSR()    # return the state of the DSR line
    getRI()    # return the state of the RI line
    getCD()    # return the state of the CD line
"""

