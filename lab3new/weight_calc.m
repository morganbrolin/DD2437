function [ W ] = weight_calc( patterns, normalize, correct_diag)

[~,N] = size(patterns);

if nargin < 3
    correct_diag = true;
end

if nargin <2
    normalize = false;
end

W = patterns'*patterns;

if normalize
    W = W./N;
end

if correct_diag
    N = size(W,1);
    W(1:N+1:end)=0;
end

end