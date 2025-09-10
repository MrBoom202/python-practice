def find_central_tendency(data):
    def find_moda(data1):
        slovnik = {}
        for number in data1:
            if number in slovnik:
                slovnik[number] += 1
            else:
                slovnik[number] = 1
        max_count = max(slovnik.values())
        moda = []
        for key in slovnik:
            if slovnik[key] == max_count:
                moda.append(key)
        return moda

    def find_median(data2):
        data2.sort()
        a = len(data2)
        mid = a // 2
        if a % 2 == 1:
            return data2[mid]
        else:
            return (data2[mid - 1] + data2[mid]) / 2
        
    def find_rozmah(data3):
        max_number = max(data3)
        min_number = min(data3)
        rozmah = max_number - min_number
        return rozmah
    print("Мода вибірки: ", find_moda(data))
    print("Медіана вибірки: ", find_median(data))
    print("Розмах вибірки: ", find_rozmah(data))

a = [5, 3, 7, 8, 1, 0, 2, 3, 8, 5, 6]
print(find_central_tendency(a))