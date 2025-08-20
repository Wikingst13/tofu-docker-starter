package test

import (
  
  "testing"

  terratestTerraform "github.com/gruntwork-io/terratest/modules/terraform"
)

func TestDevPlanNoApply(t *testing.T) {
  t.Setenv("TERRATEST_TERRAFORM_BINARY", "tofu")
  t.Setenv("AWS_ACCESS_KEY_ID", "test")
  t.Setenv("AWS_SECRET_ACCESS_KEY", "test")
  t.Setenv("AWS_DEFAULT_REGION", "us-east-1")

  opts := &terratestTerraform.Options{
    TerraformDir: "../envs/dev",
    EnvVars: map[string]string{
      "TERRATEST_TERRAFORM_BINARY": "tofu",
    },
    VarFiles: []string{"dev.tfvars"},
    NoColor: true,
  }

  // Init and plan only (no apply)
  _, err := terratestTerraform.InitAndPlanE(t, opts)
  if err != nil {
    t.Fatalf("Init/Plan failed: %v", err)
  }
}
