param(
  [string]$BaseUrl = "http://127.0.0.1:8000",
  [string]$Model = "meta-llama/Llama-3.1-8B-Instruct"
)

$modelsUrl = "$BaseUrl/v1/models"
Write-Host "Checking models endpoint: $modelsUrl"
Invoke-RestMethod -Method Get -Uri $modelsUrl | ConvertTo-Json -Depth 10

$body = @{
  model = $Model
  messages = @(
    @{ role = "system"; content = "You are a concise enterprise AI assistant." },
    @{ role = "user"; content = "Give three SLOs for an internal RAG service." }
  )
  temperature = 0.2
} | ConvertTo-Json -Depth 10

$chatUrl = "$BaseUrl/v1/chat/completions"
Write-Host "Checking chat endpoint: $chatUrl"
Invoke-RestMethod -Method Post -Uri $chatUrl -ContentType "application/json" -Body $body | ConvertTo-Json -Depth 10
