function [f_approx, abs_residual_error] = testing_and_absolute_residual_error_comp(x_test, f_test, W, mean, variance, no_of_nodes_hidden_RBF)

% Computation of Absolute Residual Error
% Detailed explanation goes here

X = x_test;                    % data for testing
f = f_test;                    % target output

N = length(x_test);
n = no_of_nodes_hidden_RBF;
miu = mean;
sigma_square = variance;

% Computation of phi matrix
phi = zeros(N,n);

for i = 1: 1:N
    for j = 1: 1:n
        phi(i,j) = exp(-(X(i)-miu(j))^2/(2*sigma_square));
    end
end

f_approx = phi*W;
residual_error = 0;
error = zeros(N,1);

for i = 1: 1: N
    error(i) = abs(f(i) -f_approx(i));
    residual_error = residual_error + error(i);
end

abs_residual_error = residual_error/N;

end

