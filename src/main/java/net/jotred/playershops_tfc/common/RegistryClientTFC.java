package net.jotred.playershops_tfc.common;

import com.talons.playershops.block.entity.custom.PlayerShopTER;
import net.jotred.playershops_tfc.common.blockentities.PlayershopsTFCBlockEntities;
import net.minecraftforge.api.distmarker.Dist;
import net.minecraftforge.client.event.EntityRenderersEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;

@Mod.EventBusSubscriber(bus = Mod.EventBusSubscriber.Bus.MOD, value = Dist.CLIENT)
public class RegistryClientTFC {
	
	@SubscribeEvent
	public static void registerBlockEntityRenderers (EntityRenderersEvent.RegisterRenderers event) {
		
		event.registerBlockEntityRenderer (PlayershopsTFCBlockEntities.PLAYER_SHOPS.get(), PlayerShopTER::new);
	}
}
