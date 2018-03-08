function [] = weight_update_seqdata_batch(X_train, ite_max,W)
% Update weight matrix during Hebbian Learning
% Detailed explanation goes here

X  = X_train;
a = size(X_train);
P = a(1);
N = a(2);
ratioArray = [0];
Iarray = [0]
for i = 1:P 
    [perchentage_match,X_out] = weight_update_batch(X_train(1:i,:), ite_max,W);
    plot(perchentage_match/i,i);
    ratioArray = [ratioArray perchentage_match];
    Iarray = [Iarray i];
end
figure(3)
plot(Iarray,ratioArray)
end

