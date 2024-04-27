// Coded by Gabriel Lima - 13/04/2024
#include <stdio.h>

/* 1086 - https://judge.beecrowd.com/en/problems/view/1086

Input:
    N M (dimensions in meters)
    L (plank width)
    K (number of planks)
    Xi...Xk (length of each plank)
    0 0 <- end input

Output:
    the smallest number of planks necessary to cover the whole floor of the ballroom
*/

int main()
{
    int n, m, k, l;
    while (scanf("%d %d", &n, &m) != EOF && n != 0 && n != 0)
    {
        scanf("%d\n%d", &l, &k);
        int x[k], i = 0, j = 0, out = 0, aux = 1, base = 0, base2 = 0, out2 = 0;
        for (i = 0; i < k; i++)
            scanf("%d", &x[i]);
        for (i = 0; i < k && aux == 1; i++)
        {
            aux = 0;
            for (j = 0; j < k - i - 1; j++)
            {
                if (x[j] < x[j + 1])
                {
                    int tmp = x[j];
                    x[j] = x[j + 1];
                    x[j + 1] = tmp;
                    aux = 1;
                }
            }
        }
        for (i = 0; i < k - 1 && base + l <= m * 100; i++)
        {
            int tmp = x[i];
            j = i + 1;
            aux = 0;
            if (tmp >= n || tmp < 0)
            {
                if (tmp == n)
                {
                    x[i] = -tmp;
                    base += l;
                    out++;
                }
                aux = 1;
            };
            while (j < k && aux == 0)
            {
                if (tmp + x[j] <= n && x[j] > 0)
                {
                    tmp += x[j];
                    x[j] = -x[j];
                    out++;
                    if (tmp == n)
                    {
                        out++;
                        base += l;
                        aux = 1;
                    }
                }
                j++;
            }
        }
        for (i = 0; i < k; i++)
        {
            if (x[i] < 0)
                x[i] = -x[i];
        }
        for (i = 0; i < k - 1 && base2 + l <= n * 100; i++)
        {
            int tmp = x[i];
            j = i + 1;
            aux = 0;
            if (tmp >= m || tmp < 0)
            {
                if (tmp == m)
                {
                    x[i] = -tmp;
                    base2 += l;
                    out2++;
                }
                aux = 1;
            };
            while (j < k && aux == 0)
            {
                if (tmp + x[j] <= m && x[j] > 0)
                {
                    tmp += x[j];
                    x[j] = -x[j];
                    out2++;
                    if (tmp == m)
                    {
                        out2++;
                        base2 += l;
                        aux = 1;
                    }
                }
                j++;
            }
        }
        if (base != n * 100 && base != m * 100 && base2 != n * 100 && base2 != m * 100)
            printf("impossivel\n");
        else
        {
            if (out < out2 && (base == n * 100 || base == m * 100))
                printf("%d\n", out);
            else
                printf("%d\n", out2);
        }
    }
    return 0;
}