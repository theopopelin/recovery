# 1 : vue compile
FROM node:24-alpine AS frontend-build

WORKDIR /frontend

COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci

COPY frontend/ ./

ARG VITE_API_URL=/recovery
ENV VITE_API_URL=${VITE_API_URL}

RUN npm run build

# 2 : prod server
FROM nginx:alpine

COPY docker/nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=frontend-build /frontend/dist /frontend/dist
