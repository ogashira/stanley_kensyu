import datetime
import platform
import sys

class DateManage(object):

    def __init__(self):
        pass


    def year_month_input(self):
        while True:
            print('\n調査月を入力してください(例_2026年9月の場合: 202609)')
            input_date = input('調査月 : ')
            if not input_date:
                print('プログラムを中止します')
                sys.exit()
            #6桁以外の数字を入力したら、強制的に終了
            if len(input_date) != 6:
                print('\nエラー: 6桁の年月を入力してください')
                continue
                
            # 3. 数字以外が混ざっていないか、および日付として正しいかのチェック
            try:
                # 4. 西暦が 2025年 〜 2100年 の間かチェック
                input_year = input_date[:4]
                input_month = input_date[4:]
                int_input_month = int(input_month)
                int_input_year = int(input_year)
                if not(2025 <= int_input_year <= 2100):
                    print("\nエラー: 西暦は2025年から2100年の間で入力してください。")
                    continue

                if not(1 <= int_input_month <= 12):
                    print("\nエラー: 月が不正です")
                    continue

                break

            except ValueError:
                # 数字以外の文字が混ざっている場合
                print("\nエラー: 正しい日付（数字のみ）を入力してください。")

        # ループを抜けた後の処理
        print(f"\n正しい調査月を受け付けました: {input_date}")
        print()
        print()

        return input_date
                

    def get_last_month_end(self, year_month: str)-> str:
        # datetimeオブジェクトに変換すると日時は自動的に１日になる。
        this_month_first_dt = datetime.datetime.strptime(year_month, "%Y%m")
        last_month_end_dt = this_month_first_dt - datetime.timedelta(days=1)
        return last_month_end_dt.strftime("%Y%m%d")

    def get_last_month(self, year_month: str)-> str:
        # datetimeオブジェクトに変換すると日時は自動的に１日になる。
        this_month_first_dt = datetime.datetime.strptime(year_month, "%Y%m")
        last_month_end_dt = this_month_first_dt - datetime.timedelta(days=1)
        return last_month_end_dt.strftime("%Y%m")

    def get_this_month_end(self, year_month: str)-> str:
        # datetimeオブジェクトに変換すると日時は自動的に１日になる。
        this_month_first_dt = datetime.datetime.strptime(year_month, "%Y%m")
        # 32日足すと必ず翌月になる
        next_month_dt = this_month_first_dt + datetime.timedelta(days=32)
        next_month_str = next_month_dt.strftime("%Y%m")
        # datetimeオブジェクトに変換すると日時は自動的に１日になる。
        next_month_first_dt = datetime.datetime.strptime(next_month_str, "%Y%m")
        this_month_end_dt = next_month_first_dt - datetime.timedelta(days=1)
        
        return this_month_end_dt.strftime("%Y%m%d")
