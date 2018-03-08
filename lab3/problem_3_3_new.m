
clear
close all
clc

% Problem 3.1_new
ite_lim = 500;

% Training Pattern
x1 = [-1 -1 1 -1 1 -1 -1 1];
x2 = [-1 -1 -1 -1 -1 1 -1 -1];
x3 = [-1 1 1 -1 -1 1 -1 1];
X = [x1; x2; x3];

% Weight Calculation
W = weight_calc(X, 0, 0);

% Patterns Update
[ x1_new, ite1 ] = update_patterns( W, x1, ite_lim );
[ x2_new, ite2 ] = update_patterns( W, x2, ite_lim );
[ x3_new, ite3 ] = update_patterns( W, x3, ite_lim );

% Check if the network is able to store all three patterns

check1 = isequal(x1_new, x1);
check2 = isequal(x2_new, x2);
check3 = isequal(x3_new, x3);

% Distorted patterns
x1d = [1 -1 1 -1 1 -1 -1 1];
x2d = [1 1 -1 -1 -1 1 -1 -1];
x3d = [1 1 1 -1 1 1 -1 1];
Xd = [x1d; x2d; x3d];

A = size(Xd);
Xd_new = zeros(A);
P = A(1);
ite = zeros(P,1);

for i = 1: P
    [Xd_new(i,:), ite(i)] = update_patterns(W, Xd(i,:), ite_lim);
end

% Number of attractors 

attractors = X;
X_test = permn([0 1],8);
X_test_new = zeros(size(X_test));

for i = 1: length(X_test)
    [X_test_new(i,:), ~] = update_patterns(W, X_test(i,:), ite_lim);
    if not(ismember(X_test_new(i,:),attractors,'rows'))
        attractors = [attractors; X_test_new(i,:)];
    end
end

% Energy computation
E_X_all = zeros(1,length(X_test));
E_attractors = zeros(1,length(attractors));

for i = 1: length(X_test)
    E_X_all(i) = energy(W, X_test(i,:));
end

for i = 1: length(attractors)
    E_attractors(i) = energy(W, attractors(i,:));
end

figure(1)
subplot(2,1,1)
plot(1:length(X_test), E_X_all,'LineWidth',2)
xlim([1 length(X_test)])
xlabel('Number of distorted patterns')
ylabel('Energy')
title('Energy at the points of the distorted patterns')
grid on

subplot(2,1,2)
plot(1:length(attractors), E_attractors,'LineWidth',2)
xlabel('Number of attractors')
ylabel('Energy')
title('Energy at different attractors')
grid on