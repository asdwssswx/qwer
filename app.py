import streamlit as st

# 애플리케이션 제목
st.title("201921054")

# 페이지 제목
st.header("임채민")
# 페이지 소제목
st.subheader("000")
# 텍스트
st.text("1234")


import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import signal

num=[6]
den=[1,4,3,0]
sys=signal.TransferFunction(num,den)


num_nonunity = [6]
den_nonunity = [1,4,3]
sys_nonunity =signal.TransferFunction(num_nonunity,den_nonunity)

w,mag,phase=signal.bode(sys)
w_nonunity,mag_nonunity,phase_nonunity=signal.bode(sys_nonunity)



import numpy as np
import matplotlib.pyplot as plt
import control

G1= control.TransferFunction([100],[1,5,6])

H1= control.feedback(G1)

t1,y1 = control.step_response(H1)

plt.figure()

plt.xlim([-0.1,2.5])
plt.ylim([0,1.2])
plt.plot(t1,y1,label='H1(s)')
plt.title('Unit Step Response with Unit Feedback Control')
plt.xlabel('Time (s)')
plt.ylabel('Response')
plt.legend()
plt.grid(True)
st.pyplot(plt)


import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


s1 = signal.lti([100],[1,5,6])

frequencies = np.logspace(-2,2,500)

w, mag, phase= s1. bode(frequencies)

plt.figure()
plt.subplot(2,1,1)
plt.semilogx(w,mag)
plt.title('Bode plot of G(s)=100/(s+2)(s+3)')
plt.ylabel('Magnitude [dB]')

plt.subplot(2,1,2)
plt.semilogx(w,phase)
plt.ylabel('Phase [degrees]')
plt.xlabel('Frequency [Hz]')


st.pyplot(plt)