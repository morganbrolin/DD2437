function [W, mean ] = batch_learning_least_square_CL_positioning_RBF( x_train, f_train , no_of_nodes_hidden_RBF, variance, CL_epoch, etha_CL)

% This code works for single dimesional data (input space)
% Detailed explanation goes here
% x and f have to be column vector

X = x_train;                        % Training data
f = f_train;                        % Target data
n_CL = CL_epoch;                    % Numbe of CL iterations
N = length(X);                      % Length of the single dimensional traing data
n = no_of_nodes_hidden_RBF;         % Number of units in the hidden RBFs
sigma_square = variance;            % Variance of gaussian RBF
 
%% Computation of phi Matrix
phi = zeros(N,n);

% Random positioning of RBF units
miu = datasample(x_train, n);

% Adjustment of positioning RBF units bt CL algorithm
for i = 1: 1: n_CL
    x_CL = datasample(x_train,1);
    proximity = zeros(n,1);
    for j = 1: 1: n
        proximity(j) = (x_CL - miu(j))^2;
    end
    ind = proximity(:) == min(proximity(:));
    wining_unit = miu(ind);
    delta = etha_CL*(x_CL - wining_unit);
    for j = 1: 1: n
        if j == ind
            miu(j) = miu(j) + delta;
        else
            miu(j) = miu(j);
        end
    end
end

% Computation of phi matrix
for i = 1: 1:N
    for j = 1: 1:n
        phi(i,j) = exp(-(X(i)-miu(j))^2/(2*sigma_square));
    end
end

%% Computation of weight Matrix
A = phi'*phi;
B = phi'*f;

% Output
W = A\B;
mean = miu;
end

