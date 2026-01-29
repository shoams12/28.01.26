# המטרה: לקלוט גילאים של 10 שחקני חטיבת ביניים לקבוצת כדורסל
#
# כללים:
#
# בצע לולאה כדי לנסות לקלוט 10 גילאים
# אם הגיל קטן מ־12 – התעלם ממנו (לא סופר כשחקן תקין) והמשך ללולאה
# אם הגיל גדול מ־18 – צא מהלולאה עם break (זה "מבוגר מדי" לקבוצת נוער) מכיוון שעלולים לפסול את הקבוצה
# אחרת – הגיל תקין וספור אותו כשחקן תקין
# אחרי הלולאה, הדפס כמה שחקנים תקינים הצלחת לאסוף. וכמה שחקנים מעל גיל 16 ספרת
valid_plyr: int = 0
abv16 = 0

while True:
    age: int = int(input("Enter player age: "))
    if valid_plyr == 10 or age > 18:
        break
    if age < 12:
        continue
    if age > 16:
        abv16 += 1

    valid_plyr += 1
print("Number of valid players: ", valid_plyr)
print("Number of players above 16 years old: ", abv16)


