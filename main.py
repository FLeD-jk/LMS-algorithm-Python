import numpy as np
import matplotlib.pyplot as plt

# Функція адаптивного алгоритму LMS
def lms_filter(d, x, mu, M):
    """
    d: бажаний сигнал (numpy array)
    x: вхідний сигнал (numpy array)
    mu: крок навчання (float)
    M: кількість коефіцієнтів фільтра (int)
    """
    N = len(x)
    w = np.zeros(M)  # початкові коефіцієнти фільтра
    y = np.zeros(N)  # вихідний сигнал фільтра
    e = np.zeros(N)  # похибка

    for n in range(M, N):
        x_vec = x[n:n-M:-1]  # вхідний вектор
        y[n] = np.dot(w, x_vec)  # вихідний сигнал фільтра
        e[n] = d[n] - y[n]  # похибка
        w += 2 * mu * e[n] * x_vec  # оновлення коефіцієнтів фільтра

    return y, e, w

# Приклад використання LMS фільтра
if __name__ == "__main__":
    # Генерація тестових сигналів
    np.random.seed(0)
    N = 500
    x = np.random.randn(N)
    d = np.convolve(x, np.array([1, -0.5]), mode='same') + 0.5 * np.random.randn(N)

    # Налаштування параметрів LMS алгоритму
    mu = 0.01
    M = 10

    # Виконання фільтрації
    y, e, w = lms_filter(d, x, mu, M)

    # Візуалізація результатів
    plt.figure(figsize=(12, 8))
    plt.subplot(2, 1, 1)
    plt.plot(d, label='Бажаний сигнал')
    plt.plot(y, label='Вихід фільтра LMS')
    plt.title('Бажаний сигнал та вихід фільтра LMS')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(e, label='Похибка')
    plt.title('Похибка фільтрації')
    plt.legend()
    plt.tight_layout()
    plt.show()
