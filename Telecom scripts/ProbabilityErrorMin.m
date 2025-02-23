clear all;
clc;

A = 1;  
T = -0.5:0.01:0.5;  % Threshold values
p = 0:0.01:1.0;  % Probability values
P_thresh_up = 0.2; % Probability threshold
P_thresh_lowe = 0.12;

% Create a grid of T and p values
[P, T_grid] = meshgrid(p, T);

% Compute probability of error
E = P .* normcdf(T_grid - A) + (1 - P) .* (1-normcdf(T_grid + A));


% Create a mask where E < P_thresh
mask = P_thresh_lowe<E < P_thresh_up;
figure;
surf(T_grid,P,E,"EdgeColor","none");
hold on;
% Create a color array: Use red where the mask is true, keep default elsewhere
C = ones(size(E, 1), size(E, 2), 3); % Initialize RGB color matrix
C(:, :, 1) = 1; % Red channel
C(:, :, 2) = 0; % Green channel
C(:, :, 3) = 0; % Blue channel

% Set transparency where mask is NOT applied
alphaData = double(mask); % Alpha is 1 where mask is true, 0 elsewhere

% Overlay the highlighted regions
surf(T_grid, P, E, C, 'EdgeColor', 'none', 'FaceAlpha', 'flat', 'AlphaData', alphaData);





%{
% Plot the full surface
figure;
surf(T_grid, P, E, 'EdgeColor', 'none'); % Normal plot
hold on;

% Overlay the masked regions with a different color (e.g., red)
highlightedE = E; 
highlightedE(~mask) = NaN; % Hide non-highlighted parts

surf(T_grid, P, highlightedE, 'FaceColor', 'red', 'EdgeColor', 'none',"FaceAlpha",0.5);
%}
% Labels and formatting
xlabel("\tau", 'FontSize', 14);
ylabel("p", 'FontSize', 14);
zlabel("Probability of error, P(E)");
title("Probability of Error Distribution", 'FontSize', 16);
colorbar;
view(3);
axis tight;
shading interp;
hold off;
