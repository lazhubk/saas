
def calc_percent(amount, days, rate) -> float:
    return round((rate / amount) * (365 / days) * 100, 4)
    
def calc_rate(amount, year, percent) -> float:
    return round(amount * percent * year / 100, 4)
    
def calc_daly_rate(reward, year) -> float:
    total_reward = reward * 1000
    total_second = year * 365 * 86400
    second_reward = total_reward / total_second
    # print(total_second, second_reward)
    return round(second_reward * 86400 / 1000, 4)

if __name__ == '__main__':
    print('#' * 50)
    
    for i in range(0, 3):
        # Perfact Setting
        section_55 = [55, 3*365, 3, 330]
        #section_55 = [550, 3*365, 3, 3465]
        #section_55 = [5500, 3*365, 3, 37950]
        #section_55 = [55000, 3*365, 3, 429000]
        #section_55 = [550000, 3*365, 3, 5280000]
        #section_55 = [3, 110*365, 110, 330]
        section_55 = [43, 10*365, 4, 330]
        psub = 100
        # section_55 = [55000, 360, 3]

        [amount, days, year, rate] = section_55
        days = days - (i * psub)
        percent = calc_percent(amount, days, rate)
        print(f'percent: {percent} - day： {days}')
        
        reward = calc_rate(amount, year, percent)
        print(f'reward: {reward}')
        
        # real_reward = calc_rate(amount, 3, percent)
        # print(f'real: {real_reward}')
        
        daily = calc_daly_rate(reward, year)
        print(f'lastest days: {days}')
        print(f'daily: {daily} - {amount / daily} \n')
    