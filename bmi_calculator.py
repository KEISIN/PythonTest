# BMI（体格指数）を計算するプログラム

def calculate_bmi(weight, height):
    """
    BMIを計算します。
    :param weight: 体重(kg)
    :param height: 身長(cm)
    :return: BMI値（小数点以下2桁）
    """
    height_m = height / 100  # cmをmに変換
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

if __name__ == "__main__":
    try:
        weight = float(input("体重(kg)を入力してください: "))
        height = float(input("身長(cm)を入力してください: "))
        bmi = calculate_bmi(weight, height)
        print(f"あなたのBMIは {bmi} です。")
    except ValueError:
        print("数値を入力してください。")