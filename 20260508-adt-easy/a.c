#include <stdio.h>

int main(void) {
  char input[4] = "";
  scanf("%s", input);

  int r = 0, m = 0, s = 0;
  int i = 0;
  for (i = 0; i < 3; i++) {
    if (input[i] == 'R') {
      r = i;
    } else if (input[i] == 'M') {
      m = i;
    } else {
      s = i;
    }
  }

  if (r < m) {
    printf("Yes");
  } else {
    printf("No");
  }
}

