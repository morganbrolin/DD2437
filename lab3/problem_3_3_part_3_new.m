

clear
close all
clc

%% Load pict.dat
A = importdata('pict.dat');
P = zeros(11,1024);

for i = 1: 1: length(A)
    if (i/1024) - floor(i/1024) == 0
        k = floor(i/1024);
    else 
        k = floor(i/1024)+1;
    end
    P(k,(i-(k-1)*1024)) = A(i);
end

P1 = reshape(P(1,:),[32 32]);
P2 = reshape(P(2,:),[32 32]);
P3 = reshape(P(3,:),[32 32]);
P4 = reshape(P(4,:),[32 32]);
P5 = reshape(P(5,:),[32 32]);
P6 = reshape(P(6,:),[32 32]);
P7 = reshape(P(7,:),[32 32]);
P8 = reshape(P(8,:),[32 32]);
P9 = reshape(P(9,:),[32 32]);
P10 = reshape(P(10,:),[32 32]);
P11 = reshape(P(11,:),[32 32]);

% Patterns
patterns = [P(1,:); P(2,:); P(3,:)];
ite_lim = 50;
Xp = P(1,:);


% Weight calculation
W = weight_calc(patterns, 0, 0);

% Noisy Pattern
X = P(1,:);
noisy_pixels = 1024;
n = noisy_pixels;
pattern_element = 1: 1: length(X);
swapidx = randsample(pattern_element, n);
X(swapidx) = X(fliplr(swapidx));
X_noisy = X; 

%[ X_new, iterations, energy ] = update_patterns1_E( W, X_noisy, Xp, ite_lim );
[ X_new, iterations, energy ] = update_patterns_latest_E( W, X_noisy, ite_lim );

plot(iterations, energy, 'LineWidth', 2)