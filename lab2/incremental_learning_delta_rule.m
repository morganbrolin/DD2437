function [W, mean] = incremental_learning_delta_rule( x_train, f_train ,no_of_nodes_hidden_RBF, variance, learning_rate, epoch)

% This code works for single dimesional data (input space)
% Detailed explanation goes here
% x and f have to be column vector

%% Given Parameter
X = x_train;                            % Training data
f = f_train;                            % Training Output
n_ite = epoch;                          % Residual error
etha = learning_rate;                   % Learning rate
N = length(X);                          % Length of the single dimensional traing data
n = no_of_nodes_hidden_RBF;             % Number of units in the hidden RBF
sigma_square = variance;                % Variance of gaussian RBF

% Algorithm: Incremental Laerning by Delta Rule
miu= datasample(x_train,n);
Wa = rand (n,1);
k = 1;
while k < n_ite
    for i = 1: 1: N
    xk = X(i);
    phi_xk = zeros(n,1);
    for j = 1: 1: n
        phi_xk(j) = exp(-(xk - miu(j))^2/(2*sigma_square));
    end
    e = (f(i) - phi_xk'*Wa);
    delta_W = etha*e*phi_xk;
    Wa = Wa + delta_W;
    end
    k = k + 1;
end
% Output
mean = miu;
W = Wa;
end

