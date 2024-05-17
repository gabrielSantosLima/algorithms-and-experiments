#include <stdio.h>

int main()
{
    int t = 0, n = 0, d = 0, i = 0, r = 0, tt = 0, tmp = 0, tmp2 = 0, ant = 0, prox = 0;
    char aux = 'B';
    scanf("%d", &t);
    while (tt < t)
    {
        scanf("%d %d", &n, &d);
        int p[n];

        for (i = 0; i < n; i++)
        {
            scanf(" %c-%d", &aux, &p[i]);
            if (aux == 'S')
                p[i] *= -1;
        }

        r = 0;
        i = 0;
        ant = 0;
        tmp = 0;
        prox = 0;

        while (i < n)
        {
            tmp2 = p[i];
            if (tmp2 < 0)
                tmp2 *= -1;

            if (i == n - 1)
                prox = d;
            else if (p[i] < 0)
            {
                prox = p[i + 1];
                if (prox < 0)
                    prox *= -1;
            }

            if (i == 0)
            {
                r = tmp2;
                ant = tmp2;
            }
            else if (prox - ant <= tmp2 && p[i] < 0)
            {
                if (prox - ant >= r)
                    r = prox - ant;
                if (p[tmp] < 0)
                    p[tmp] = 0;
                ant = prox;
                tmp = i + 1;
                i++;
            }
            else
            {
                if (tmp2 - ant >= r)
                    r = tmp2 - ant;
                if (p[tmp] < 0)
                    p[tmp] = 0;
                ant = tmp2;
                tmp = i;
            }
            i++;
        }

        if (d - ant > r)
            r = d - ant;
        if (p[tmp] < 0)
            p[tmp] = 0;

        i = n - 1;
        ant = d;
        while (i >= 0)
        {
            tmp2 = p[i];
            if (tmp2 < 0)
                tmp2 *= -1;
            if (tmp2 != 0)
            {
                if (ant - tmp2 > r)
                    r = ant - tmp2;
                ant = tmp2;
            }
            i--;
        }
        if (ant > r)
            r = ant;
        printf("Case %d: %d\n", tt + 1, r);
        tt++;
    }
    return 0;
}