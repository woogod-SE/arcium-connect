use anchor_lang::prelude::*;

declare_id!("Fg6PaFpoGXkYsidMpWTK6W2BeZ7FEfcYkg476zPFsLnS");

#[program]
pub mod arcium_registry {
    use super::*;
    pub fn register_user(ctx: Context<RegisterUser>, hashed_id: [u8; 32]) -> Result<()> {
        let user_record = &mut ctx.accounts.user_record;
        user_record.wallet_address = *ctx.accounts.user.key;
        user_record.hashed_id = hashed_id;
        Ok(())
    }
}

#[derive(Accounts)]
pub struct RegisterUser<'info> {
    #[account(init, payer = user, space = 8 + 32 + 32, seeds = [b"record", user.key().as_ref()], bump)]
    pub user_record: Account<'info, UserRecord>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[account]
pub struct UserRecord {
    pub wallet_address: Pubkey,
    pub hashed_id: [u8; 32],
}
