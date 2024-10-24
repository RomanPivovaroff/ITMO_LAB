def cod_xem_7_4(message):
    message_list = [int(i) for i in message]
    s1 = (message_list[0] + message_list[2] + message_list[4] + message_list[6]) % 2
    s2 = (message_list[1] + message_list[2] + message_list[5] + message_list[6]) % 2
    s3 = (message_list[3] + message_list[4] + message_list[5] + message_list[6]) % 2
    position_error = {1, 2, 3, 4, 5, 6, 7}
    if s1:
        position_error = position_error.intersection({1, 3, 5, 7})
    else:
        position_error = position_error - {1, 3, 5, 7}
    if s2:
        position_error = position_error.intersection({2, 3, 6, 7})
    else:
        position_error = position_error - {2, 3, 6, 7}
    if s3:
        position_error = position_error.intersection({4, 5, 6, 7})
    else:
        position_error = position_error - {4, 5, 6, 7}
    if position_error:
        error = list(position_error)[0]
        message = message[:error - 1] + str((int(message[error - 1]) + 1) % 2) + message[error:]
    else:
        error = 'ошибок нет'
    return message[2] + message[4:7], message, (f"позиция ошибки: {error}")


print(cod_xem_7_4('0001100'))
print(cod_xem_7_4('1001011'))
print(cod_xem_7_4('0001101'))
print(cod_xem_7_4('1010110'))
print(cod_xem_7_4('0000000'))