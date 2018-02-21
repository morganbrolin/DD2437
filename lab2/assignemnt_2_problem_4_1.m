
clear;
close all;
clc

%% Topological ordering of animal species

% Given parameters
no_of_nodes = 100;
no_of_epochs = 20;
size_of_neighbourhood = 5;
learning_rate = 0.2;

% Import Data
A = importdata('animals.dat');
B = importdata('animalnames.txt');

% Making data in the desired form
a = length(A);
row_num = 32;
col_num = 84;
data = zeros(row_num,col_num);

for i = 1: 1: a
    if (i/col_num) - floor(i/col_num) ~= 0
        j = 1 + floor(i/col_num);
    else
        j = floor(i/col_num);
    end
    k = i - (j-1)*col_num;
    data(j,k) = A(i);
end

WIN = som(data, no_of_nodes, no_of_epochs, size_of_neighbourhood, learning_rate);
[C, I] = sort(WIN);
B_ordered = cell(row_num,1);
for i = 1: 1: row_num
    b = I(i);
    B_ordered(i) = B(b);
end
