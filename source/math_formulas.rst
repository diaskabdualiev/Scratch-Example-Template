.. _math-section:

=======================
Математические формулы
=======================

Sphinx поддерживает LaTeX математические формулы через расширение MathJax.

Inline математика
=================

Формулы в строке записываются так: :math:`E = mc^2` или :math:`a^2 + b^2 = c^2`.

Также можно использовать более сложные выражения: :math:`\sum_{i=1}^{n} x_i = x_1 + x_2 + \ldots + x_n`.

Block математика
================

Для блочных формул используется директива `.. math::`:

.. math::

   \int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}

Квадратичная формула:

.. math::

   x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}

Формула Эйлера:

.. math::

   e^{i\pi} + 1 = 0

Системы уравнений
=================

.. math::

   \begin{cases}
   x + y = 5 \\
   2x - y = 1
   \end{cases}

Матрицы
=======

Простая матрица:

.. math::

   A = \begin{pmatrix}
   1 & 2 & 3 \\
   4 & 5 & 6 \\
   7 & 8 & 9
   \end{pmatrix}

Определитель матрицы:

.. math::

   \det(A) = \begin{vmatrix}
   a & b \\
   c & d
   \end{vmatrix} = ad - bc

Суммы и произведения
====================

Сумма ряда:

.. math::

   S = \sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}

Произведение:

.. math::

   \prod_{i=1}^{n} x_i = x_1 \cdot x_2 \cdot \ldots \cdot x_n

Пределы:

.. math::

   \lim_{x \to \infty} \frac{1}{x} = 0

   \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n = e

Интегралы
=========

Определенный интеграл:

.. math::

   \int_0^1 x^2 dx = \frac{1}{3}

Неопределенный интеграл:

.. math::

   \int e^x dx = e^x + C

Двойной интеграл:

.. math::

   \iint_D f(x,y) \, dx \, dy

Производные
===========

Производная функции:

.. math::

   \frac{d}{dx} x^n = nx^{n-1}

Частные производные:

.. math::

   \frac{\partial f}{\partial x} = \lim_{h \to 0} \frac{f(x+h,y) - f(x,y)}{h}

Градиент:

.. math::

   \nabla f = \left( \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z} \right)

Дроби и корни
=============

Сложные дроби:

.. math::

   \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{\ddots}}}}

Корни:

.. math::

   \sqrt{x^2 + y^2}

   \sqrt[n]{x}

Тригонометрия
=============

Основные функции:

.. math::

   \sin^2 x + \cos^2 x = 1

   \tan x = \frac{\sin x}{\cos x}

Формула Эйлера для тригонометрии:

.. math::

   e^{ix} = \cos x + i \sin x

Логарифмы
=========

.. math::

   \log_a b = \frac{\ln b}{\ln a}

   \log_a (xy) = \log_a x + \log_a y

Статистика и вероятность
========================

Нормальное распределение:

.. math::

   f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}

Биномиальное распределение:

.. math::

   P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}

Формула Байеса:

.. math::

   P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}

Сложные примеры
===============

Формула Стирлинга:

.. math::

   n! \approx \sqrt{2\pi n} \left(\frac{n}{e}\right)^n

Преобразование Фурье:

.. math::

   F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i\omega t} dt

Уравнение Шрёдингера:

.. math::

   i\hbar \frac{\partial \Psi}{\partial t} = \hat{H} \Psi

Нумерация уравнений
===================

Уравнения можно нумеровать:

.. math::
   :label: euler_formula

   e^{i\pi} + 1 = 0

.. math::
   :label: pythagoras

   a^2 + b^2 = c^2

Ссылка на уравнение: см. уравнение :eq:`euler_formula`.

Align окружения
===============

Выравнивание по знакам:

.. math::

   \begin{align}
   x &= a + b + c \\
   &= d + e \\
   &= f
   \end{align}

Система с выравниванием:

.. math::

   \begin{align}
   2x + 3y &= 7 \\
   x - y &= 1
   \end{align}

Специальные символы
===================

Греческие буквы: :math:`\alpha, \beta, \gamma, \delta, \epsilon, \zeta, \eta, \theta, \lambda, \mu, \pi, \sigma, \phi, \chi, \psi, \omega`

Операторы: :math:`\pm, \mp, \times, \div, \cdot, \circ, \bullet, \star`

Отношения: :math:`\leq, \geq, \neq, \approx, \equiv, \sim, \propto`

Множества: :math:`\in, \notin, \subset, \supset, \cup, \cap, \emptyset, \infty`

Стрелки: :math:`\leftarrow, \rightarrow, \leftrightarrow, \Leftarrow, \Rightarrow, \Leftrightarrow` 