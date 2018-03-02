function [weight_matrix, ite] = weight_update_batch(X_train, learning_rate, ite_max)
% Update weight matrix during Hebbian Learning
% Detailed explanation goes here

X  = X_train;
a = size(X_train);
P = a(1);
N = a(2);
ratioArray = [0];
Iarray = [0]
for i = 1:P 
    [weight_matrix, ite] = weight_update_batch(X_train(1:i,:), learning_rate, ite_max);
    plot(ite/i,i)
    ratioArray = [ratioArray ite];
    Iarray = [Iarray i];
end
figure(3)
plot(Iarray,ratioArray)
end

