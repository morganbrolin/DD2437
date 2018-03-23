
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
patterns = [P(1,:); P(2,:); P(3,:);P(4,:)];
[p, N] = size(patterns);
ite_lim = 10;

% Weight calculation
W = weight_calc(patterns, 0, 1);

[ P1_degraded_new, ite1 ] = update_patterns( W, P(1,:), ite_lim );
[ P2_degraded_new, ite2 ] = update_patterns( W, P(2,:), ite_lim );

P1_degraded = reshape(P1_degraded_new,[32 32]);
P2_degraded = reshape(P2_degraded_new,[32 32]);

figure(1)

subplot(2,1,1)
imagesc(P10)
title('4 datapoints')
subplot(2,1,2)
imagesc(P1_degraded)


figure(2)
subplot(2,1,1)
imagesc(P11)
title('4 datapoints')
subplot(2,1,2)
imagesc(P2_degraded)







