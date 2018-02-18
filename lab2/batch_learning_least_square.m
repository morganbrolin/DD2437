function [W, mean ] = batch_learning_least_square( x_train, f_train , no_of_nodes_hidden_RBF, variance)

% This code works for single dimesional data (input space)
% Detailed explanation goes here
% x and f have to be column vector

X = x_train;                        % Training data

N = length(X);                      % Length of the single dimensional traing data
n = no_of_nodes_hidden_RBF;         % Number of units in the hidden RBFs
sigma_square = variance;            % Variance of gaussian RBF
 
%% Computation of phi Matrix

miu = datasample(x_train, n);
phi = zeros(N,n);

for i = 1: 1:N
    for j = 1: 1:n
        phi(i,j) = exp(-(X(i)-miu(j))^2/(2*sigma_square));
    end
end

%% Computation of weight Matrix
A = phi'*phi;
B = phi'*f_train;
W = A\B;
mean = miu;
end

