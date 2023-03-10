#implementacion hecha para micropython basado en https://morf.lv/implementing-pulse-oximeter-using-max30100

def moving_average(values, window):
    #media movil
    i = 0
    moving_averages = []
    
    while i < len(values) - window + 1:
        window_arr = values[i : i + window]
      
        # Calculate the average of current window
        window_average = round(sum(window_arr) / window, 2)  
        moving_averages.append(window_average)
        i += 1
    return(moving_averages) 
    
    

def calculate_spo2(red_list, ir_list, window_size):
        
    # Media movil para mejor estabilidad de senal
    red_filtered = moving_average(red_list, window_size)
    ir_filtered = moving_average(ir_list, window_size)
    
    red_dc = sum(red_filtered) / len(red_filtered)
    ir_dc = sum(ir_filtered) / len(ir_filtered)
    
    ratio = red_dc / ir_dc
    #print('ratio:',ratio) "Debug" para calibracion manual
    
    #coeficientes obtenidos de 5 sensores versus oximetro comercial y reloj garmin en 2 personas
    #a = 3.7691 and b = -78.5114
    
    #la constance C=0 debe usarse para calibracion exacta en otros sensores
    
    spo2 = 3.7691+78.5114*ratio+0
    #valores obtenidos por calibracion manual, mas info: https://morf.lv/implementing-pulse-oximeter-using-max30100
    # y paper: https://d1wqtxts1xzle7.cloudfront.net/50231726/jeas_0915_2598-libre.pdf?1478787679=&response-content-disposition=inline%3B+filename%3DINTEGRATION_OF_LOW_COST_SpO2_SENSOR_IN_A.pdf&Expires=1676146508&Signature=DwE1mC-4Rq8nh1~8i~ez5JmBjxyvJ0nvQSi2zUalXkwHA7n2C0zmxUkycXfe4qhvMhA5hnLlWvafW~fTGP8Z-7jme8hmGu-wWoIFKhrjjYnIIl95e7FhHv87kSnfKQ0Ma7B7rygnZ6Nh0L2U7BFMp0Vin7IoB8kd~wCrWFStkBKqHgD9xRcFB0HaxKMofJfhYjERn~XDSsnuFwqALOGyHwuNVOLQR9CLlDJ8oAIDAHEzn8IFthnNsTHimHsGstzun~CIoSlnBm9NmBrPmDHXzaZcXRNyaE-l2DT5dMmq5Gou-cBXmPDPNS7XEKCyFATwpXwfb-6lV-rqo4ZUTsxe9g__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA

    return spo2
