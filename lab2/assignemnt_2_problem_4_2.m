 
clear;
close all;
clc;

%% Cyclic Tour

% Given parameters
no_of_epochs = 40;
size_of_neighbourhood = 2;
learning_rate = 0.2;

% Import Data
A = importdata('cities.dat');
B = importdata('citynames.txt');
A = cell2mat(A(3:end));
city_position = str2num(A);
row_num = 10;
col_num = 2;
data = city_position;

WIN = som_circular_neighbour(data, no_of_epochs, size_of_neighbourhood, learning_rate);
[C, I] = sort(WIN);
B_ordered = cell(row_num,1);
for i = 1: 1: row_num
    b = I(i);
    B_ordered(i) = B(b);
end
city_ordered = zeros(row_num, col_num);

for i = 1: 1: row_num
    b = I(i);
    city_ordered(i,:) = city_position(b,:);
end


% Plot
city_ordered_size = size(city_ordered);
dcity_oredred = zeros(city_ordered_size);

for i = 1: 1: row_num
    if i ~= row_num
        dcity_oredred(i,:) = city_ordered(i+1,:)- city_ordered(i,:);
    else
        dcity_oredred(i,:) = 0;
    end
end

quiver(city_ordered(:,1),city_ordered(:,2),dcity_oredred(:,1),dcity_oredred(:,2),0,'r', 'LineWidth',2)
xlabel('x')
ylabel('y')
title('Cyclic Tour')
grid on;

