function [W, mean, no_of_nodes_hidden_RBF] = batch_learning_least_square_new( x_train, f_train , absolute_residual_error, variance)

% This code works for single dimesional data (input space)
% Detailed explanation goes here
% x and f have to be column vector

%% Given Parameter
X = x_train;                            % Training data
f = f_train;                            % Training Output
are_lim = absolute_residual_error;      % Absolute residual error
N = length(X);                          % Length of the single dimensional traing data
sigma_square = variance;                % Variance of gaussian RBF
 
n = 0;
are = are_lim + 1 ;

while are > are_lim
    n = n+1;
    miu= datasample(x_train,n);
    phi = zeros(N,n);
    for i = 1: 1:N
        for j = 1: 1:n
            phi(i,j) = exp(-(X(i)-miu(j))^2/(2*sigma_square));
        end
    end
    A = phi'*phi;
    B = phi'*f_train;
    Wa = A\B;
    f_approx = phi*Wa;
    residual_error = 0;
    for i = 1: 1: N
        error = abs(f(i) - f_approx(i));
        residual_error = residual_error + error;
    end
    are = residual_error/N;
end

no_of_nodes_hidden_RBF = n;
mean = miu;
W = Wa;
end

