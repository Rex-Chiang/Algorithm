import numpy as np
import matplotlib.pyplot as plt

# 以下定義變數x的目標函式
def Fit_func(x):
    f= 10*np.sin(x)/x
    
    return f

# 以下定義函式來執行PSO程序
def PSO():      
    # 以下初始化粒子數、權重，並設定 x、速率 的上下限
    particle_cnt=30
    x_position= []
    Average_x= []
    ws=0.9; c1=1; c2=1
    r1=np.random.randn()*0.1; r2=np.random.randn()*0.1
    max_x= 15
    min_x= -15
    maxv=5
    
    pos= np.random.random_sample([particle_cnt])*200
    v0=np.random.random_sample([particle_cnt])
    
    # 以下給予20顆粒子的pbest初始值
    pbest=pos
    # 以下定義gbest的初始值
    pbestfit=Fit_func(pbest)
    
    gbestfit= max(pbestfit)
    pbestfit= list(pbestfit)    
    gbest= pbest[pbestfit.index(gbestfit)]
    
    # 以下開始移動並更新速率及位置，預設迭代100次
    for k in range(0, 100):
        V = (ws*v0)+(c1*r1*(pbest-pos))+(c2*r2*(gbest-pos))
        # 以下判斷速率有無超過上下限 
        for i in range(0, particle_cnt):
            if V[i] > maxv:
                V[i] = maxv
            elif V[i] < -maxv:
                V[i] = -maxv
        
        X = pos + V
        # 以下判斷位置有無超過上下限  
        for i in range(0,particle_cnt):
            if X[i] > max_x:
                X[i] = max_x
            elif X[i] < min_x:
                X[i] = min_x
                
        # 以下速率更新
        v0=V
        # 以下位置更新
        pos=X
        # 以下個體適應值更新
        prefit= Fit_func(pbest)
        nowfit= Fit_func(X)
       
        for i in range(0, particle_cnt):
            if nowfit[i] > prefit[i]:
                pbest[i]= pos[i]
   
        pbestfit=  Fit_func(pbest)
        
        # 以下群體適應值更新
        if max(pbestfit) > gbestfit:
            gbestfit= max(pbestfit)
            pbestfit= list(pbestfit)
            gbest= pbest[pbestfit.index(gbestfit)]#,:]
            
        Average_x.append(sum(pbest)/particle_cnt)
        x_position.append(gbest)
    
    return x_position, Average_x

# 以下為主執行程式及輸出繪圖
if __name__ == '__main__': 
    x_position1, Average_x= PSO()
    x_position2,_= PSO()
    
    print("Particle 1's positions : \n")
    for i in range(0, len(x_position1)):
        if i < 10:
            print(x_position1[i])
        elif i==11:
            print(".\n.\n.\n.\n")
        elif 19 < i < 30:
            print(x_position1[i])
    
    print("\nParticle 2's positions : \n")
    for i in range(0, len(x_position2)):
        if i < 10:
            print(x_position2[i])
        elif i==11:
            print(".\n.\n.\n.\n")
        elif 19 < i < 30:
            print(x_position2[i])
    
    plt.plot(x_position1)
    plt.plot(x_position2, "r--")
    plt.axis([-3, 30, -10, 10])
    plt.xlabel("Iterations")
    plt.ylabel("x-position")
    plt.legend(("Particle 1", "Particle 2"), loc= "upper right")
    plt.grid(color='g',linestyle='--', linewidth=1,alpha=0.4)
    plt.show()
    
    print("\n********************Next fig********************")
    
    Best_Fitness= Fit_func(x_position1)
    Average_Fitness= Fit_func(Average_x)
    
    print("Best Fitness's data : \n")
    for i in range(0, len(Best_Fitness)):
        if i < 10:
            print(Best_Fitness[i])
        elif i==11:
            print(".\n.\n.\n.\n")
        elif 19 < i < 30:
            print(Best_Fitness[i])
    
    print("\nAverage Fitness's data : \n")
    for i in range(0, len(Average_Fitness)):
        if i < 10:
            print(Average_Fitness[i])
        elif i==11:
            print(".\n.\n.\n.\n")
        elif 19 < i < 30:
            print(Average_Fitness[i])
    
    plt.plot(Best_Fitness)
    plt.plot(Average_Fitness, "r--")
    plt.axis([-3, 27, 1.5, 11])
    plt.xlabel("Iterations")
    plt.ylabel("Fitness")
    plt.legend(("Best Fitness", "Average Fitness"), loc= "lower right")
    plt.grid(color='g',linestyle='--', linewidth=1,alpha=0.4)
    plt.show()