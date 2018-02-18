
clear;
close all;
clc;

%% Assignment-2, Part-1 , Problem 3.1
% Batch learning using method of least squares

% Parameters
%absolute_residual_error = 0.1;
no_of_nodes_hidden_RBF = 10;
epoch = 5000;
learning_rate = 0.02;
variance = 5;


% Training data set
x_train = (0 : 0.1: (2*pi))';
f_train = sin(x_train);

% Testing data set
x_test = (0.05 : 0.1: (2*pi))';
f_test = sin(x_test);

% Computing weight Matrix
%[W, mean] = batch_learning_least_square( x_train, f_train , no_of_nodes_hidden_RBF, variance);
%[W, mean, no_of_nodes_hidden_RBF] = batch_learning_least_square_new( x_train, f_train , absolute_residual_error, variance);
[W, mean] = incremental_learning_delta_rule( x_train, f_train ,no_of_nodes_hidden_RBF, variance, learning_rate, epoch);

% computing approximated output for testing data set and absolute residual
% error

[f_approx, abs_residual_error] = testing_and_absolute_residual_error_comp(x_test, f_test, W, mean, variance, no_of_nodes_hidden_RBF);

figure(1)
plot(x_test, f_test,'b', x_test, f_approx, '-.r*', 'LineWidth', 2)
xlim([0 2*pi])
%ylim([-1.5 1.5])
xlabel('x')
ylabel('sinx')
legend('function','approximated function')
text(1.6*pi,0.8,sprintf('abs residual error = %0.6f',abs_residual_error))
grid on;
