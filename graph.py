import matplotlib.pyplot as plt
from Code import start1


Ear_Values,Mar_Values,Time_value=start1()

plt.plot(Time_value, Ear_Values,label="EAR Values")
plt.xlabel('Time')
plt.ylabel('MAR & EAR')
plt.title("E.A.R. & M.A.R. ratios with respect to time")
plt.plot(Time_value, Mar_Values, label="MAR Values")
plt.legend()
plt.show()
