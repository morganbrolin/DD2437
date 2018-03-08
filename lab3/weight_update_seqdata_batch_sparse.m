function [activity] = weight_update_seqdata_batch_sparse(X_train, ite_max,bias)

X  = X_train;
a = size(X_train);
P = a(1);
N = a(2);
ratioArray = [0];
Iarray = [0]
for i = 1:P 
    [W,activity] = weight_calc_sparse(X_train(1:i,:),0,0);
    [X_new,ite] = update_patterns_sparse( W, X_train(1:i,:), ite_max,bias );
    perchentage_match = sum(sum(abs(X_train(1:i,:)-X_new)')==0);
    ratioArray = [ratioArray perchentage_match/i];
    Iarray = [Iarray i];
end
figure(1)
plot(Iarray,ratioArray)
end

