#include <stdio.h>

int main() {
    char name[50], department[50];
    int empId;
    float basicSalary, DA, HRA, TA, grossSalary, netSalary;

    printf("Enter Employee Name: ");
    fgets(name, sizeof(name), stdin);

    printf("Enter Employee ID: ");
    scanf("%d", &empId);

    getchar();

    printf("Enter Department: ");
    fgets(department, sizeof(department), stdin);

    printf("Enter Basic Salary: ");
    scanf("%f", &basicSalary);

    DA = 0.92 * basicSalary;
    HRA = 0.58 * basicSalary;
    TA = 0.30 * basicSalary;

    grossSalary = basicSalary + DA + HRA + TA;
    netSalary = grossSalary - 500;

    printf("\n----- Employee Details -----\n");
    printf("Name       : %s", name);
    printf("Employee ID: %d\n", empId);
    printf("Department : %s", department);

    printf("\n----- Salary Details -----\n");
    printf("Basic Salary : %.2f\n", basicSalary);
    printf("DA (92%%)     : %.2f\n", DA);
    printf("HRA (58%%)    : %.2f\n", HRA);
    printf("TA (30%%)     : %.2f\n", TA);
    printf("LIC Deduction: 500.00\n");
    printf("Net Salary   : %.2f\n", netSalary);

    return 0;
}
