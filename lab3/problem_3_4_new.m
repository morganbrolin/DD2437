
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
[p, N] = size(patterns);
pattern_element = 1: 1: N;
ite_lim = 50000;

% Weight calculation
W = weight_calc(patterns, 0, 0);

Xp = P(1,:);
noisy_pixels = [0, 10, 50, 100, 200, 400, 500, 700, 850, 950, 1024];

for n = noisy_pixels
    swapidx = randsample(pattern_element, n);
    figure;
    X = P(1,:);
    if n ~= 0
        X(swapidx) = X(fliplr(swapidx));
    end
    X_noisy = X;
    X_noisy_plot = reshape(X_noisy,[32 32]);
    subplot(1,2,1);
    imagesc(X_noisy_plot);
    title(sprintf('Flipping %.2f percent of the pixels of p1',...
        n/N*100));
    % Update rule by Morgan
    [X_final, ite] = update_patterns_latest(W, X_noisy, ite_lim);
    % Update rule by Avbhishek
    %[X_final, ite] = update_patterns1(W, X_noisy, Xp, ite_lim);
    X_final = reshape(X_final,[32 32]);
    subplot(1,2,2);
    imagesc(X_final);
    title(sprintf('Result after %d iterations', ite));
end
