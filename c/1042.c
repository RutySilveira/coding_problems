#include <stdio.h>

int main() {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);

    int ao = a;
    int bo = b;
    int co = c;
    int aux;

    if (ao > bo) {
        aux = ao;
        ao = bo;
        bo = aux;
    }
    if (ao > co) {
        aux = ao;
        ao = co;
        co = aux;
    }
    if (bo > co) {
        aux = bo;
        bo = co;
        co = aux;
    }

    printf("%d\n", ao);
    printf("%d\n", bo);
    printf("%d\n\n", co);

    printf("%d\n", a);
    printf("%d\n", b);
    printf("%d\n", c);

    return 0;
}
