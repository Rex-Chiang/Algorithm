import numpy as np
import matplotlib.pyplot as plt

def DEA(n= 9, m_size= 20, f=0.5, cr=0.3, iterate_times= 100, x_min= np.zeros(9), x_max= np.ones(9)*10):
    x_position= []
    # 產生所有x的初始資料庫
    x_all= np.zeros((iterate_times+1, m_size, n))
    # 依照DE演算法隨機產生初始群體
    for i in range(m_size):
        x_all[0][i]= x_min + np.random.random()*(x_max - x_min)

    print("Initialize sucessfully !!")
    
    for g in range(iterate_times):
        print(">>iteration of", g+1, "<<")
        for i in  range(m_size):
            # 排除目前所處理的群體
            x_without_i= np.delete(x_all[g], i, 0)
            
            # 將x中的數據按照隨機順序重排，打散數據
            np.random.shuffle(x_without_i)
            
            # 變異操作(Mutation)
            # 對第g代隨機抽取3個組成新的變異個體，由於已打亂數據，固定索引依然代表隨機選取
            m_i= x_without_i[1]+ f*(x_without_i[2]- x_without_i[3])
            
            # 檢查m_i是否超過所設置的上下限
            m_i= [m_i[item] if m_i[item] < x_max[item] else x_max[item] for item in range(n)]
            m_i= [m_i[item] if m_i[item] > x_min[item] else x_min[item] for item in range(n)]
        
            # 交叉操作(Crossover)
            # 根據隨機數以及交叉閥執，對新的變異個體以及目前所處理的個體進行參數混合，確定最後的個體
            v_i= np.array([x_all[g][i][j] if (np.random.random() > cr) else m_i[j] for j in range(n)])
      
            # 選擇操作(Selection)
            # 若最後個體的適應值優於目前所處理的個體的適應值，則在下一代中取代目前所處理個體
            if Fit_func(x_all[g][i]) > Fit_func(v_i):
                x_all[g+1][i]= v_i
                
            else:
                
                x_all[g+1][i]= x_all[g][i]
                
        evaluate_result= [Fit_func(x_all[g][i]) for i in range(m_size)]
        # 取出evaluate_result中最小值的索引值
        best_x= x_all[g][np.argmin(evaluate_result)]
        x_position.append(best_x)
        #print(evaluate_result)
        print(best_x)
    return x_position

def Fit_func(x):
    f=0
    x= np.transpose(x)
    for i in range(0, len(x)):
        f=f+(x[i]-(i+1))**2
    return f

if __name__ == "__main__":
    
    f= []
    x_position= DEA()
    # 索引出最終之最佳值
    Final_best= x_position[99]
    # 預設迭代100次, X軸
    iteration= np.arange(0, 100)
    # 目標函數值, Y軸
    for i in range(0, len(x_position)):
        f.append(Fit_func(x_position[i]))

    plt.plot(iteration, f)
    plt.xlabel("Iterations")
    plt.ylabel("f(x)")
    plt.grid(color='g',linestyle='--', linewidth=1,alpha=0.4)
    plt.show()
    
    print("\nx's positions : \n")
    for i in Final_best:
        print("x"+str(list(Final_best).index(i)+1)+":",i)