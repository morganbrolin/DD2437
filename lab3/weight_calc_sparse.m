function [ W ] = weight_calc_sparse( patterns, normalize, correct_diag)

[P,N] = size(patterns);

if nargin < 3
    correct_diag = true;
end

if nargin <2
    normalize = false;
end
activity = (1/N*P)*sum(sum(patterns));
patterns = patterns - activity;
W = patterns'*patterns;

if normalize
    W = W./N;
end

if correct_diag
    W = W - diag(W);
end

end