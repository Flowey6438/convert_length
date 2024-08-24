def convert_length(value, from_unit, to_unit):
    # 定义单位转换比例（基准为米）
    conversion_factors = {
        '米': 1,
        '千米': 0.001,
        '英里': 0.000621371,
        '英尺': 3.28084,
        '厘米': 100,
        '毫米': 1000,
        '码': 1.09361,
        '英寸': 39.3701
    }
    
    # 将输入的值转换为米
    value_in_meters = value * conversion_factors[from_unit]
    
    # 将米转换为目标单位
    converted_value = value_in_meters / conversion_factors[to_unit]
    
    return converted_value

if __name__ == "__main__":
    print("欢迎使用长度单位转换器！")
    try:
        value = float(input("请输入要转换的长度数值："))
        from_unit = input("请输入原单位（米、千米、英里、英尺、厘米、毫米、码、英寸）：")
        to_unit = input("请输入目标单位（米、千米、英里、英尺、厘米、毫米、码、英寸）：")
        
        if from_unit in ['米', '千米', '英里', '英尺', '厘米', '毫米', '码', '英寸'] and to_unit in ['米', '千米', '英里', '英尺', '厘米', '毫米', '码', '英寸']:
            converted_value = convert_length(value, from_unit, to_unit)
            print(f"{value} {from_unit} 等于 {converted_value:.4f} {to_unit}")
        else:
            print("无效的单位，请输入正确的单位名称。")
    except ValueError:
        print("无效的数值输入，请输入有效的数字。")
